import fem.geometry as fegeom
import matplotlib.pyplot as plt

geomlist=[
        ('+','circle',0.0,0.0,1.0,10),
        ('+','circle',1.0,0.0,1.0,10),
        ('-','circle',0.5,0.0,0.2,5)#,
        #('-','box',0.6,0,2.0,2.0)
        ]

g=fegeom.GeometryShapelyTriangle2D(geomlist)

g.process()

mesh=g.mesh(0.4)

g.draw()
mesh.plot()

plt.show()