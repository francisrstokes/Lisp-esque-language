const symbols = require('./symbols');

module.exports = [
  [/^[\s\n]+$/, symbols.SKIP],
  [/^;.+?\n$/, symbols.SKIP],
  [/^\($/, symbols.LPAREN],
  [/^\)$/, symbols.RPAREN],
<<<<<<< HEAD
  [/^\-?[0-9]+\.?[0-9]*$/, symbols.NUMBER],
=======
  [/^[0-9]+$/, symbols.NUMBER],
>>>>>>> c7473bddffd1d8e1c1bd5c860b29a3a2dfcf4fd8
  [/^\"[^\n\"]*\"$/, symbols.STRING],
  [/^(T|F)$/, symbols.BOOLEAN],
  [/^[a-zA-Z\+\-\/\*\_\>\<=]*$/, symbols.IDENTIFIER],
];
