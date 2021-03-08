/**
 * @license Copyright (c) 2003-2020, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	CKEDITOR.config.extraPlugins = "imageresize";
	CKEDITOR.config.imageResize = { 
		maxWidth : 800, maxHeight : 800 
	};
	CKEDITOR.config.width = '100%';
};
