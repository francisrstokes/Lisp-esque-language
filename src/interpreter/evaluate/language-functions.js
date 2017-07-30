const createScope = require('./create-scope');

const scopedFunction = (bodyExpressions = [], expectedArguments = [], scope = {}) => [
  func,
  expectedArguments,
  scope
];

module.exports = {
  print: (scope, value) => {
    process.stdout.write(value);
  },
  let: (scope, name, value) => {
    if (scope.variables.name) {
      throw new Error(`Error. Can't overwrite previously assigned scoped variable '${name}'`);
    }
    if (scope.functions.name) {
      throw new Error(`Error. Can't overwrite scoped function '${name}' with variable declaration.`);
    }
    scope.variables[name] = value;
  },
  function: (scope, name, expectedArguments, bodyExpressions) => {
    const functionScope = createScope(scope);
    scope.functions[name] = scopedFunction(bodyExpressions, expectedArguments, functionScope);
  },
  '+': (scope, x, y) => x + y,
  '-': (scope, x, y) => x - y,
  '/': (scope, x, y) => x / y,
  '*': (scope, x, y) => x * y
};
