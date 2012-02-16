var dataView;
var grid;
var data = [];

var options = {
    editable: true,
    enableColumnReorder:false,
    asyncEditorLoading:true,
    forceFitColumns:false
};

function log(val) {
    console.log(val);
}

function list_collections() {
    $.getJSON('/collections/', function (collections) {
        $('#set_collection_name').empty();
        $(collections).each(function (index) {
            var d = collections[index];
            var o = $('<option/>').val(d).text(d);
            $('#set_collection_name').append(o);
        });
        get_items(current_collection());
    })
}

function current_collection() {
    return $('#set_collection_name').find(':selected').val();
}

function add_item(collection, item) {
    $.ajax({
               url:'/collections/' + collection,
               type:'POST',
               data:item,
               dataType:'JSON',
               success:function (response) {
                   log(response);
                   get_items(collection);
               }
           })
}

function get_items(collection) {

    $.ajax({
               url:'/collections/' + collection,
               dataType:'json',
               cache:false,
               success:function (items) {
                   var item, key, val;
                   var new_data = [];
                   $(items).each(function (index) {
                       item = items[index];
                       key = item[0];
                       val = item[1];
                       new_data.push(
                           {
                               "id":key,
                               "title":val['title'],
                               "duration":val['duration']

                           })
                   });
                   dataView.beginUpdate();
                   dataView.setItems(new_data);
                   grid.invalidateAllRows();
                   dataView.endUpdate();
                   grid.render();
               }
           })

}

function delete_item(id) {
    var url = "/collections/" + current_collection() + "/" + id;
    log("delete: " + url);
    $.ajax({
               url:url,
               type:'DELETE',
               success:function () {
                   get_items(current_collection());
               }
           });
}

$(function () {

    $('#add_item_form').submit(function () {
        var curr = current_collection();
        var item = $('#add_item_name').val();
        add_item(curr, item);
        return false;
    });

    // Handle a change in collection
    $('#set_collection_name').bind('change', function () {
        get_items(current_collection());
    });


    $('#delete_all').click(function () {
        var url;
        var coll_name = current_collection();
        $.getJSON('/collections/' + coll_name, function (data) {
            var id;
            $.each(data, function (key, val) {
                // Issue a DELETE request for item in collection
                id = val[0];
                url = "/collections/" + coll_name + '/' + id;
                $.ajax({
                           url:url,
                           type:'DELETE'
                       });
            })
        })
    });
    $('#reload').click(function () {
        get_items(current_collection());
    });

    // Get the columns via ajax, then the data
    $.ajax({
               url:'test-columns.json',
               dataType:'JSON',
               cache:false,
               success:function (columns) {
                   // Now get the data
                   dataView = new Slick.Data.DataView();
                   grid = new Slick.Grid(".slickGrid",
                                         dataView,
                                         columns,
                                         options);
                   grid.setSelectionModel(new Slick.RowSelectionModel());
                   list_collections();
                   // Bind delete
                   grid.onKeyDown.subscribe(function (e) {
                       if (e.which == 46) {
                           // Delete was pressed
                           var sel = grid.getSelectedRows()[0];
                           var item = dataView.getItem(sel);
                           delete_item(item.id);
                       }
                   });

               }
           });


});
