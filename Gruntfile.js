module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        appDir: 'outingbox/',
        staticDir: '<%= appDir %>static/',
        devDir: '<%= appDir %>dev/',
        templatesDir: '<%= appDir %>templates/',
        browserify: {
            dist: {
                files: {
                    '<%= devDir %>outingbox/js/bundle.js': '<%= devDir %>outingbox/js/script.js'
                }
            },
        },
        sass: {
            options: {
                precision: 8,
                'unix-newlines': true
            },
            dist: {
                files: {
                    '<%= devDir %>outingbox/css/styles.css': '<%= devDir %>outingbox/sass/styles.scss'
                }
            }
        },
        concat: {
            dist: {
                src: [
                    '<%= devDir %>vendor/css/font-awesome.min.css',
                    '<%= devDir %>vendor/css/slick.css',
                    '<%= devDir %>vendor/css/slick-theme.css',
                    '<%= devDir %>vendor/css/fontawesome-stars.css',
                    '<%= devDir %>vendor/css/sweetalert.css',
                    '<%= devDir %>vendor/css/selectize.bootstrap3.css',
                    '<%= devDir %>outingbox/css/styles.css'
                ],
                dest: '<%= devDir %>outingbox/css/bundle.css'
            },
        },
        cssmin: {
            options: {
                report: 'gzip',
                keepSpecialComments: 0
            },
            css: {
                src: '<%= devDir %>outingbox/css/bundle.css',
                dest: '<%= staticDir %>outingbox/css/bundle.min.css'
            }
        },
        uglify: {
            js: {
                files: {
                    '<%= staticDir %>outingbox/js/bundle.min.js': ['<%= devDir %>outingbox/js/bundle.js']
                }    
            }
        },
        watch: {
            options: {
                livereload: true
            },
            src: {
                files: ['<%= templatesDir %>**/*.html'],
                tasks: []
            },
            css: {
                files: ['<%= devDir %>outingbox/sass/*.scss'],
                tasks: ['sass', 'concat', 'cssmin']
            },
            js: {
                files: ['<%= devDir %>outingbox/js/*.js', '!<%= devDir %>outingbox/js/bundle.js'],
                tasks: ['browserify', 'uglify']  
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-browserify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('build', ['sass', 'concat','cssmin', 'browserify','uglify']);
};
