const createScope = require('./create-scope');
const languageFunctions = require('./language-functions');
const globalScope = createScope(null);
const stack = [];

module.exports = (ast) => {
  // Scope rules
  // Language scope -> scope -> upperScope (ascend)
};
