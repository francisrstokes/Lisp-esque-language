const evaluateExpr = require('./evaluate-expr');
const stack = require('./stack');
const getScope = () => stack[stack.length - 1];

module.exports = (ast) =>{
  ast.forEach(expr =>
    evaluateExpr(getScope(), expr)
  );
}