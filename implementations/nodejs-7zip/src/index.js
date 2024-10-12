const path = require('path')
const Seven = require('node-7z')
const fs = require('fs')
const cliProgress = require('cli-progress')

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
  const outputPath = path.join(outputDir, `nodejs-7zip-${Date.now()}.zip`)

  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true })
  }

  const progressBar = new cliProgress.SingleBar(
    {
      format: 'Progress [{bar}] {percentage}%'
    },
    cliProgress.Presets.shades_classic
  )

  const seven = Seven.add(outputPath, `${inputDir}/*.pdf`, {
    $progress: true,
    recursive: true
  })

  progressBar.start(100, 0)

  seven.on('progress', function (progress) {
    progressBar.update(progress.percent)
  })

  seven.on('end', function () {
    progressBar.stop()
    console.log(`Compression completed. Output file: ${outputPath}`)
  })

  seven.on('error', function (err) {
    progressBar.stop()
    console.error('An error occurred:', err)
  })
}

zipPdfs().catch(console.error)
