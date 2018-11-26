from flask import Flask
from flask import Blueprint

route_imooc = Blueprint( 'imooc_page',__name__)

@route_imooc.route("/")
def imooc():
    return "imooc index page"



