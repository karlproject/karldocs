var grid;

var options = {
    enableCellNavigation:true,
    enableColumnReorder:false
};

$(function () {
    // Get the columns via ajax, then the data
    $.ajax({
               url:'demo1-columns.json',
               dataType:'JSON',
               cache:false,
               success:function (columns) {
                   // Now get the data
                   $.ajax({
                              url:'demo1-simple.json',
                              dataType:'JSON',
                              cache:false,
                              success:function (data) {
                                  grid = new Slick.Grid(".slickGrid", data, columns, options);
                              }
                          });
               }
           });
})
