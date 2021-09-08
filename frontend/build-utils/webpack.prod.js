const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
    mode: "production",
    resolve: {
        extensions: ['.js', '.jsx'],
      },
    plugins: [
        new MiniCssExtractPlugin()
    ],
    
    optimization: {
        minimize: true,
        minimizer: [
          new CssMinimizerPlugin(),
        ],
      },
}