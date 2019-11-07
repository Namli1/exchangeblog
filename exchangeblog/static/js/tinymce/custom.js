tinymce.init({
    selector : 'textarea',
    resize: 'both',
    theme: 'silver',
    plugins : 'link image media lists autoresize fullscreen template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime wordcount advlist lists checklist',
    autoresize_bottom_margin: 50,
    file_picker_types: 'file image media',
    toolbar: 'undo redo | styleselect | bold italic | link image | alignleft aligncenter alignright alignjustify | fullpage',
    menu: {
        file: { title: 'File', items: 'restoredraft | preview | print ' },
        edit: { title: 'Edit', items: 'undo redo | cut copy paste | selectall wordcount' },
        insert: { title: 'Insert', items: 'image link media template codesample | inserttable tableprops deletetable row column cell| charmap emoticons hr | pagebreak nonbreaking anchor toc | insertdatetime' },
        format: { title: 'Format', items: 'bold italic underline strikethrough superscript subscript codeformat | formats blockformats fontformats fontsizes align | forecolor backcolor | removeformat' },
          }
})



/* tinymce.init({
    selector: 'textarea#id_blogcontent',
    plugins: 'print preview fullpage paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars e^ticons',
    menubar: 'file edit view insert format tools table help',
    toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl',
    toolbar_sticky: true,
    autosave_ask_before_unload: true,
    importcss_append: true,
    height: 400,
    height: 600,
    image_caption: true,
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    toolbar_drawer: 'sliding',
    contextmenu: "link image imagetools table",
   }); */