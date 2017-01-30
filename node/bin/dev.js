#!/usr/bin/env node

var fs = require('fs');
var childProcess = require('child_process');

try {
  if (!fs.statSync('./dev').isFile()) {
    throw new Error('No dev file');
  }

  fs.accessSync('./dev', fs.constants.X_OK);
}
catch (e) {
  console.log('There is no executable dev script to run.');
  process.exit()
}

var result = childProcess.spawnSync('./dev', process.argv.slice(2), {
  stdio: 'inherit'
});

process.exit(result.status);
