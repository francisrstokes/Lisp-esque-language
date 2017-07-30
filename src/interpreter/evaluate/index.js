const evaluateExpr = require('./evaluate-expr');
const rootScope = require('./create-scope')(null);

<<<<<<< HEAD
module.exports = (ast) => ast.forEach(expr => evaluateExpr(rootScope, expr));
=======
module.exports = (ast) => {
  // console.log(ast)
  ast.forEach(expr =>
    evaluateExpr(rootScope, expr)
  );
}
>>>>>>> c7473bddffd1d8e1c1bd5c860b29a3a2dfcf4fd8
