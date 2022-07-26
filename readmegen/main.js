const path = require('path');
const fs = require('fs');
const util = require('util');
const readdir = util.promisify(fs.readdir);

//joining path of directory 
const mdFile = path.join(__dirname, '..', 'readme.md');

const directories = ['exercises/leetcode', 'exercises/hackerrank', 'exercises/facebookrecruiting'];


const getExercises = async function(mainFolderName) {
  const mainFolderPath = path.join(__dirname, '..', mainFolderName);
  const files = await readdir(mainFolderPath);
  const directories = []
  files.forEach(function (file) {
      // Do whatever you want to do with the file
      const filePath = path.join(mainFolderName, file)
      const st = fs.statSync(filePath);
      if (st.isDirectory()) {
        directories.push({file, path: filePath})
      }
  });
  return directories;
}

const createMdSection = (title, listItems) => {
  let markdown = ['## '+title, '']

  markdown.push(
    (listItems.map(dr => {
      return `- [${dr.file}](${dr.path})`
    })).join("\n")
  );
  return markdown;
}


const createMdFile = (markdown) => {
  fs.writeFile(mdFile, markdown.join("\n"), function (err) {
    if (err) return console.log(err);
    console.log('Hello World > helloworld.txt');
  });
}


const final = async _ => {
  const leetExe = await getExercises(directories[0])  
  const leetMd = createMdSection('Leetcode', leetExe)

  const hackerrankExercise = await getExercises(directories[1])  
  const hackMd = createMdSection('HackerRank', hackerrankExercise)

  const facebookExercise = await getExercises(directories[2])  
  const facebookMd = createMdSection('HackerRank', facebookExercise)

  const finalMd = [
    '# Code Katas',
    '',
    ...leetMd,
    '',
    ...hackMd,
    '',
    ...facebookMd
  ]

  createMdFile(finalMd)
}

final()

