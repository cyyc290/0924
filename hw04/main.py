import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,n):

        n = int(n) if n is not None else 9

        html='''
        <html>
        <body>
        <table  border="1" >
        '''
        
        for i in range(1,n+1):
            html += '<tr >'
            for j in range(1,i+1):
                html += '<td> %3d x %3d = %3d  </td>' % (j,i,i*j)
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
