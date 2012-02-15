var grid;

var options = {
    enableCellNavigation:true,
    enableColumnReorder:false
};

function log(val) {
    console.log(val);
}

function list_collections() {
    $.ajax({
               url:'/collections/',
               dataType:'JSON',
               cache:false,
               success:function (collections) {
                   $('#set_collection_name').empty();
                   $(collections).each(function (index) {
                       var d = collections[index];
                       var o = $('<option/>').val(d).text(d);
                       $('#set_collection_name').append(o);
                   })
               }
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
               dataType:'JSON',
               cache:false,
               success:function (items) {
                   log(items);
                   set_grid(items);
               }
           })

}

function set_grid(items) {
    var item;
    var key;
    var val;
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
    grid.setData(new_data);
    grid.render();
}

$(function () {

    // First, get the current list of collections
    list_collections();

    $('#add_item_form').submit(function () {
        var curr = current_collection();
        var item = $('#add_item_name').val();
        add_item(curr, item);
        return false;
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
                   $.ajax({
                              url:'test-items.json',
                              dataType:'JSON',
                              cache:false,
                              success:function (data) {
                                  grid = new Slick.Grid(".slickGrid", data, columns, options);
                              }
                          });
               }
           });
});
