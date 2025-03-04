const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development', // Or 'production' for production builds
  entry: './src/index.jsx',
  output: {
    path: path.resolve(__dirname, 'dist'), // Absolute path to the output directory
    filename: 'bundle.js',
    publicPath: '/',
  },
  devtool: 'inline-source-map', // For easier debugging
  devServer: {
    static: {
      directory: path.join(__dirname, '.'), // Serve from project root
    },
    port: 3000,
    historyApiFallback: true,
    hot: true,
  },
  resolve: {
    extensions: ['.js', '.jsx'],
    modules: [path.resolve(__dirname, 'src'), 'node_modules'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif|ico)$/,
        type: 'asset/resource',
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, 'index.html'),
      filename: 'index.html',
    }),
  ],
};

