var dataView;
var grid;
var data = [];
var columns = [
    {id:"sel", name:"#", field:"num", behavior:"select",
        cssClass:"cell-selection", width:40, cannotTriggerInsert:true,
        resizable:false, selectable:false },
    {id:"title", name:"Title", field:"title", width:120, minWidth:120,
        cssClass:"cell-title", editor:Slick.Editors.Text,
        validator:requiredFieldValidator, sortable:true},
    {id:"duration", name:"Duration", field:"duration",
        editor:Slick.Editors.Text, sortable:true}
];

var options = {
    editable:true,
    enableAddRow:true,
    enableCellNavigation:true,
    asyncEditorLoading:true,
    forceFitColumns:true,
    topPanelHeight:25
};

var sortcol = "title";
var sortdir = 1;
var searchString = "";

function requiredFieldValidator(value) {
    if (value == null || value == undefined || !value.length) {
        return {valid:false, msg:"This is a required field"};
    }
    else {
        return {valid:true, msg:null};
    }
}

function myFilter(item, args) {
    if (args.searchString != "" && item["title"].indexOf(args.searchString) == -1) {
        return false;
    }

    return true;
}

function comparer(a, b) {
    var x = a[sortcol], y = b[sortcol];
    return (x == y ? 0 : (x > y ? 1 : -1));
}

function toggleFilterRow() {
    if ($(grid.getTopPanel()).is(":visible")) {
        grid.hideTopPanel();
    } else {
        grid.showTopPanel();
    }
}


$(".grid-header .ui-icon")
    .addClass("ui-state-default ui-corner-all")
    .mouseover(function (e) {
                   $(e.target).addClass("ui-state-hover")
               })
    .mouseout(function (e) {
                  $(e.target).removeClass("ui-state-hover")
              });

$(function () {
    // prepare the data
    for (var i = 0; i < 50; i++) {
        var d = (data[i] = {});

        d["id"] = "id_" + i;
        d["num"] = i;
        d["title"] = "Task " + i;
        d["duration"] = "5 days";
    }


    dataView = new Slick.Data.DataView({ inlineFilters:true });
    grid = new Slick.Grid("#myGrid", dataView, columns, options);
    grid.setSelectionModel(new Slick.RowSelectionModel());

    var columnpicker = new Slick.Controls.ColumnPicker(columns, grid, options);


    // move the filter panel defined in a hidden div into grid top panel
    $("#inlineFilterPanel")
        .appendTo(grid.getTopPanel())
        .show();

    grid.onCellChange.subscribe(function (e, args) {
        dataView.updateItem(args.item.id, args.item);
    });

    grid.onAddNewRow.subscribe(function (e, args) {
        var item = {"num":data.length, "id":"new_" + (Math.round(Math.random() * 10000)),
            "title":"New task", "duration":"1 day"
        };
        $.extend(item, args.item);
        dataView.addItem(item);
    });

    grid.onKeyDown.subscribe(function (e) {
        // select all rows on ctrl-a
        if (e.which != 65 || !e.ctrlKey) {
            return false;
        }

        var rows = [];
        for (var i = 0; i < dataView.getLength(); i++) {
            rows.push(i);
        }

        grid.setSelectedRows(rows);
        e.preventDefault();
    });

    grid.onSort.subscribe(function (e, args) {
        sortdir = args.sortAsc ? 1 : -1;
        sortcol = args.sortCol.field;

        // using native sort with comparer
        // preferred method but can be very slow in IE with huge datasets
        dataView.sort(comparer, args.sortAsc);
    });

    // wire up model events to drive the grid
    dataView.onRowCountChanged.subscribe(function (e, args) {
        grid.updateRowCount();
        grid.render();
    });

    dataView.onRowsChanged.subscribe(function (e, args) {
        grid.invalidateRows(args.rows);
        grid.render();
    });

    var h_runfilters = null;

    // wire up the search textbox to apply the filter to the model
    $("#txtSearch2").keyup(function (e) {
        Slick.GlobalEditorLock.cancelCurrentEdit();

        // clear on Esc
        if (e.which == 27) {
            this.value = "";
        }

        searchString = this.value;
        updateFilter();
    });

    function updateFilter() {
        dataView.setFilterArgs({
                                   searchString:searchString
                               });
        dataView.refresh();
    }

    $("#btnSelectRows").click(function () {
        if (!Slick.GlobalEditorLock.commitCurrentEdit()) {
            return;
        }

        var rows = [];
        for (var i = 0; i < 10 && i < dataView.getLength(); i++) {
            rows.push(i);
        }

        grid.setSelectedRows(rows);
    });


    // initialize the model after all the events have been hooked up
    dataView.beginUpdate();
    dataView.setItems(data);
    dataView.setFilterArgs({searchString:searchString});
    dataView.setFilter(myFilter);
    dataView.endUpdate();

    // if you don't want the items that are not visible (due to being filtered out
    // or being on a different page) to stay selected, pass 'false' to the second arg
    dataView.syncGridSelection(grid, true);

    $("#gridContainer").resizable();
})