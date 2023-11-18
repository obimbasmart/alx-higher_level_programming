#!/usr/bin/node

const fileSys = require('fs');

const fileAContent = fileSys.readFileSync(process.argv[2], 'utf-8');
const fileBContent = fileSys.readFileSync(process.argv[3], 'utf-8');

fileSys.writeFileSync(process.argv[4], fileAContent + fileBContent);
