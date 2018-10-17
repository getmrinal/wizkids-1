var name;

document.getElementById('reorder').onclick = function () {
  var d = document.getElementsByClassName('ord');
  name = '';
  for (var i = 0; i < d.length; i++) {
    console.log(d[i].innerHTML);
    name += String(d[i].innerHTML).trim();
  }
  document.getElementById('setvalue').value = name;
  $.ajax({
    url: "reord",
    data: {
      'content': name
    },
    dataType: 'text',
    success: function (response) {
      console.log("Done shuffling " + response);
      OnSuccess();
    }
  });
}

function OnSuccess() {
  var p = $("#idcourse").val();
  console.log(p);
  knowtopics(p);
  // var tcontent = `<table id="sort" class="grid table table-striped table-dark table-hover" title="Magic Table">
  //   <thead>
  //           <tr><th class="index" scope="col">Topic Title</th><th>Description</th></tr>
  //   </thead>
  //       <tbody>`;
  // $.ajax({
  //   url: "topic",
  //   data: {
  //     'content': p
  //   },
  //   dataType: 'json',
  //   success: function (response) {
  //     $.each(response, function () {
  //       console.log(response);
  //       tcontent += `<tr><td hidden="true" class="index" scope="row">  </td><td style="display:none" class="ord">${this.fields.oid}</td> <td>${this.fields.title}</td> <td>
  //               <button class="btn btn-success" onclick="capmodal(${this.pk})" data-toggle="modal" data-target="#topicdesc">View</button>
  //               <input id="${this.pk}" hidden="true" value="${this.fields.desc}" />
  //             </td><td><button class="btn btn-success" id="knowcontent" onclick="showcontent(${this.pk})" type="submit">Know Content</button></td><td><span class="navbar-toggler-icon"></span></td></tr>`;
  //     });
  //     tcontent += `</tbody></table>`;

  //     $.get("/static/css/reorder.css", function (css) {
  //       $('<style type="text/css"></style>')
  //         .html(css)
  //         .appendTo("head");
  //     });

  //     $("#showtable").html(tcontent);

  //     $.getScript("https://code.jquery.com/jquery-1.12.4.js", function () {
  //       console.log("Script-1 loaded");
  //       $.getScript("https://code.jquery.com/ui/1.12.1/jquery-ui.js", function () {
  //         console.log("Script-2 loaded");
  //         $.getScript("/static/js/reorder.js", function () {
  //           console.log("Script-3 loaded");
  //         });
  //       });
  //     });
  //     var buttons = `<button class="btn btn-success" data-toggle="modal" data-target="#addcourse">Add Topic</button><button id="reorder" class="btn btn-success">Re-Order</button><input type="text" hidden="true" name="setvalue" id="setvalue" value="initial value" /><input type="text" hidden="true" id="idcourse" value="${p}" />`;
  //     $("#setbuttons").html(buttons);
  //     $.getScript("/static/js/creator-reorder.js", function () {
  //       console.log("reorder working!");
  //     });
  //   }
  // });
}

function showcontent(id) {
  console.log(id);
  var topicContent = `
  <table class="grid table table-stripped table-dark table-hover">
      <thead>
      
      </thead>
      <tbody>`;
  var contentt = `<table id="sort" class="grid table table-striped table-dark table-hover" title="Magic Table">
  <thead>
          <tr><th class="index" scope="col">Topic Title</th><th>Description</th></tr>
  </thead>
      <tbody>`;
  $.ajax({
    url: "res",
    data: {
      'content': id
    },
    dataType: 'json',
    success: function (response) {
      var rsjson = JSON.parse(response['rsjson']);
      var tsjson = JSON.parse(response['tsjson']);
      $.each(tsjson, function () {
        if (this.pk == id) {
          console.log(this.fields.cid);
          topicContent += `
            <tr>
              <td style = "background:#28a745"; >${this.fields.title}</td>
              <tr>
              `;
        } else {
          topicContent += `
            <tr>
              <td onclick="showcontent(${this.pk})" >${this.fields.title}</td>
              <tr>
              `;
        }
      });
      $.each(rsjson, function () {
        contentt += `
          <tr>
        <td class="index" scope="row">
          ${this.fields.oid}
        </td>
        <td  class="ord">
          ${this.fields.oid}
        </td>
        <td>
          ${this.fields.code}
        </td>
        <td id="${this.pk}">
          <script type="text/javascript">
          
          var obj = ${this.fields.data};

            if("${this.fields.code}" == "Q"|| "${this.fields.code}" == "T")
            {
              //console.log(obj.content.question);
              document.getElementById("${this.pk}").innerHTML = obj.content.question + "<br>" + obj.content.answer;
            }
            else if("${this.fields.code}" == "V" || "${this.fields.code}" == "P")
            {
              if("${this.fields.code}" == "V")
              {
                console.log(obj.url);
                document.getElementById("${this.pk}").innerHTML = '<video controls preload="none" src="' + obj.url + '" ></video>';
              }
              else if("${this.fields.code}" == "P")
              {
                document.getElementById("${this.pk}").innerHTML = '<img src="' + obj.url + '" width="10%" height="20%" alt="some image" >';
              }
            }
            else if("${this.fields.code}" == "M"){
              document.getElementById("${this.pk}").innerHTML = obj.ques;
            }
          </script>

        </td>
        <td>
        <span class="navbar-toggler-icon"></span>
      </td>
      </tr>
          `;
      });
      contentt += `</tbody></table>`;
      topicContent += `</tbody></table>`;
      $.get("/static/css/reorder.css", function (css) {
        $('<style type="text/css"></style>')
          .html(css)
          .appendTo("head");
      });

      $("#showtable").html(contentt);
      $("#justforres").html(topicContent);
      document.getElementById('justforres').style = "display:block;"


      $.getScript("https://code.jquery.com/jquery-1.12.4.js", function () {
        console.log("Script-1 loaded");
        $.getScript("https://code.jquery.com/ui/1.12.1/jquery-ui.js", function () {
          console.log("Script-2 loaded");
          $.getScript("/static/js/reorder.js", function () {
            console.log("Script-3 loaded");
          });
        });
      });
      var buttons = `<div class="container">
        <div class="row">
          <div class="col-md-3">
            <button class="btn btn-success" data-toggle="modal" data-target="#addresource2">Add text/Questions</button>
          </div>
          <div class="col-md-3">
              <button class="btn btn-success" data-toggle="modal" data-target="#addresource">Add Video/Pictures</button>
          </div>
      
          <div class="col-md-3">
              <button class="btn btn-success" data-toggle="modal" data-target="#addresource3">Add MCQ</button>
          </div>
      
          <div class="col-md-3">
              <form action="" method="get">
              <button onclick="func()" class="btn btn-success">Re-Order</button>
              <input type="text" hidden=true name="setvalue" id="setvalue" value="initial value" />
            </form>
          </div>
        </div>
      </div>`;
      $("#setbuttons").html(buttons);
      $.getScript("/static/js/creator-reorder.js", function () {
        console.log("reorder working!");
      });
    }
  });
}