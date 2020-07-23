body {
    font-family: Arial;
    margin: 0;
    padding: 20px;
    background-color: #f1f1f1;
}

* {
    box-sizing: border-box;
}

.row:after {
    content: '';
    display: table;
    clear: both;
}

header {
    background-color: #ffffff;
    padding: 2px;
}

header h1 {
    text-align: center;
    font-size: 60px;
    color: #000000;
    margin: 1.5 0px;
}

h2 {
    color: #000000;
    margin: 1.5 0px;
}

.left-column {
    float: left;
    width: 35%;
}

.right-column {
    width: 25%;
    float: left;
    padding-left: 20px;
}

.card {
    padding: 20px;
    background-color: #ffffff;
    margin-top: 20px;
}

.card img {
    width: 40%;
}

.right-column .card img {
    margin-bottom: 10px;
}

footer {
    background-color: #dddddd;
    padding: 20px;
    text-align: center;
    margin-top: 20px;
}


/*responsive */

@media(max-width:800px) {
    .left-column,
    .right-column {
        width: 50%;
        padding: 0px;
    }
}