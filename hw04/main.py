import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,n):

        n = int(n) if n is not None else 9
        m = int(self.get_argument('n',10))
        if m in range(1,10):
            n=m
        html='''
        <html>
        <body>
        <table  frame="void" border="1" cellspacing="2" cellpadding="5" >
        '''
        
        for i in range(1,n+1):
            html += '<tr >'
            for j in range(1,i+1):
                html += '<td> %d x %d = %d  </td>' % (j,i,i*j)
            html += '</tr>'
        html+= '''
        </table>
        </body>
        </html>
        '''
        self.write(html)

application = tornado.web.Application([
    (r"/([0-9])?", MainHandler),
],debug=True)


if __name__ == "__main__": 
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
