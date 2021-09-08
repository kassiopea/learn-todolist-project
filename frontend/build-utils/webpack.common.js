const path = require('path');
const HTMLWebpackPlugin = require('html-webpack-plugin');
const { CleanPlugin } = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: path.resolve[__dirname, "..", "./src/index.jsx"],
    output: {
        path: path.resolve(__dirname, "..", "./dist"),
        filename: "[name].[fullhash].js",
        publicPath: "/"
    },
    devServer: {
        port: 3000,
        historyApiFallback: true
    },
    resolve: {
        extensions: ['.js', '.jsx'],
      },
    plugins: [
        new HTMLWebpackPlugin({
            template: path.resolve(__dirname, "..", "./src/index.html"),
        }),
        new CleanPlugin(),
        new MiniCssExtractPlugin()
    ],

    module: {
        rules: [
             {
                test: /\.(css|less)$/,
                use: [MiniCssExtractPlugin.loader, "css-loader", "less-loader"]
            },
            {
                test: /\.(jpg|jpeg|png|svg)/,
                use: ['file-loader']
            },
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ["babel-loader"]
              }
        ]
    }
}