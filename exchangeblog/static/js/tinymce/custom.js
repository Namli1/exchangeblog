tinymce.init({
    selector : 'textarea',
    resize: 'both',
    plugins : 'link image media lists autoresize fullscreen template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime wordcount advlist lists checklist',
    autoresize_bottom_margin: 50,
    images_upload_url: { "location": "static/uploads/new-photo-test.png" },
    file_picker_types: 'file image media',
    automatic_uploads: true,
    toolbar: 'undo redo | styleselect | bold italic | link image | alignleft aligncenter alignright alignjustify | fullpage',
    menu: {
        file: { title: 'File', items: 'restoredraft | preview | print ' },
        edit: { title: 'Edit', items: 'undo redo | cut copy paste | selectall wordcount' },
        insert: { title: 'Insert', items: 'image link media template codesample | inserttable tableprops deletetable row column cell| charmap emoticons hr | pagebreak nonbreaking anchor toc | insertdatetime' },
        format: { title: 'Format', items: 'bold italic underline strikethrough superscript subscript codeformat | formats blockformats fontformats fontsizes align | forecolor backcolor | removeformat' },
          },
})