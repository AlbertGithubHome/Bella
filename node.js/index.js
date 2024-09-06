/**
 * Module dependencies
 */

var fs = require('fs');

function async (err, files) {
    console.log(files)
}

fs.readdir(__dirname, async)