CKEDITOR.addTemplates( 'default',
{
	// The name of the subfolder that contains the preview images of the templates.
	imagesPath : CKEDITOR.getUrl( CKEDITOR.plugins.getPath('templates' ) + 'templates/images/' ),

	// Template definitions.
	templates :
		[
			{
				title: 'Country Guide Template',
				image: 'country-guide.svg',
				description: 'Use this for writing a country guide.',
				html:
					'<h1>Question 1</h1>' +
                    '<p>Text here.</p>' +
                    '<h1>Question 2</h1>' +
                    '<p>Text here.l</p>'
			},
		]
});