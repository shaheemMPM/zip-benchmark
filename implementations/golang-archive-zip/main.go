package main

import (
	"archive/zip"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func zipPDFs(inputDir, outputDir string) (string, error) {
	if err := os.MkdirAll(outputDir, os.ModePerm); err != nil {
		return "", err
	}

	timestamp := time.Now().Format("20060102_150405")
	zipFilename := filepath.Join(outputDir, fmt.Sprintf("golang-archive-zip-%s.zip", timestamp))

	zipFile, err := os.Create(zipFilename)
	if err != nil {
		return "", err
	}
	defer zipFile.Close()

	zipWriter := zip.NewWriter(zipFile)
	defer zipWriter.Close()

	err = filepath.Walk(inputDir, func(filePath string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() {
			return nil
		}
		if !strings.HasSuffix(strings.ToLower(info.Name()), ".pdf") {
			return nil
		}

		relPath, err := filepath.Rel(inputDir, filePath)
		if err != nil {
			return err
		}

		zipFile, err := zipWriter.Create(relPath)
		if err != nil {
			return err
		}

		fsFile, err := os.Open(filePath)
		if err != nil {
			return err
		}
		defer fsFile.Close()

		_, err = io.Copy(zipFile, fsFile)
		return err
	})

	if err != nil {
		return "", err
	}

	fmt.Printf("Zip file created: %s\n", zipFilename)
	return zipFilename, nil
}

func main() {
	inputDir := filepath.Join("..", "..", "common", "test_data", "sample_pdfs")
	outputDir := filepath.Join("..", "..", "output")

	_, err := zipPDFs(inputDir, outputDir)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}
}
