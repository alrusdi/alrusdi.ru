'use strict';

const gulp = require('gulp');
const babel = require('gulp-babel');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');

const dirs = {
  src: 'static',
  dest: 'static'
};

const sassPaths = {
  src: `${dirs.src}/sass/*.sass`,
  dest: `${dirs.dest}/build/css/`
};

const jsPaths = {
  src: `${dirs.src}/js/app/*.js`,
  dest: `${dirs.dest}/build/js/`
};

gulp.task('styles', () => {
  return gulp.src(sassPaths.src)
    .pipe(sourcemaps.init())
    .pipe(sass({indentedSyntax: true}))
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(sassPaths.dest));
});

gulp.task('js', () => {
  return gulp.src(jsPaths.src)
    .pipe(sourcemaps.init())
    .pipe(babel({
            presets: ['@babel/env']
    }))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(jsPaths.dest));
});

gulp.task('watch', () => {
    gulp.watch(sassPaths.src, ['styles', 'js']);
});

gulp.task('static', ['styles', 'js']);