const fs = require('fs')
const path = require('path')
const JSZip = require('jszip')

const inputDir = path.join(
  __dirname,
  '..',
  '..',
  '..',
  'common',
  'test_data',
  'sample_pdfs'
)
const outputDir = path.join(__dirname, '..', '..', '..', 'output')

async function zipPdfs () {
  const zip = new JSZip()
  const pdfFiles = fs
    .readdirSync(inputDir)
    .filter((file) => path.extname(file).toLowerCase() === '.pdf')

  for (const file of pdfFiles) {
    const filePath = path.join(inputDir, file)
    const fileContent = fs.readFileSync(filePath)
    zip.file(file, fileContent)
  }

  const outputPath = path.join(outputDir, `nodejs-jszip-${Date.now()}.zip`)
  const output = fs.createWriteStream(outputPath)

  zip
    .generateNodeStream({ type: 'nodebuffer', streamFiles: true })
    .pipe(output)
    .on('finish', function () {
      console.log(`Zipped ${pdfFiles.length} PDF files to ${outputPath}`)
    })
}

zipPdfs().catch(console.error)
