from flask import Flask, request
from flask_restful import Resource, Api
import getAllNodesFunction, getLocationsFunction, getNodeFunction
import deleteNodeFunction
import createNodeFuntion
import resizeNodeFunction
import shutdownNodeFunction, startNodeFunction, rebootNodeFunction

app = Flask(__name__)
api = Api(app)



@app.route('/GetAllNodes', methods=['POST','GET'])
def GetAllNodes():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']

		nodes = getAllNodesFunction.getAllNodes(provider,driverUno,driverDos,driverTres,driverCuatro)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/GetLocations', methods=['POST','GET'])
def GetLocations():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']

		nodes = getLocationsFunction.getLocations(provider,driverUno,driverDos,driverTres,driverCuatro)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/GetNode', methods=['POST','GET'])
def GetNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		nodeId = request.form['nodeId']

		nodes = getNodeFunction.getNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/DeleteNode', methods=['POST','GET'])
def DeleteNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		nodeId = request.form['nodeId']

		nodes = deleteNodeFunction.deleteNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/CreateNode', methods=['POST','GET'])
def CreateNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		name = request.form['name']
		size = request.form['size']
		image = request.form['image']
		location = request.form['location']
		ex_network = request.form['ex_network']

		nodes = createNodeFuntion.createNode(provider,driverUno,driverDos,driverTres,driverCuatro,name,size,image,location,ex_network)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/ResizeNode', methods=['POST','GET'])
def ResizeNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		size = request.form['size']
		nodeId = request.form['nodeId']
		
		nodes = resizeNodeFunction.resizeNode(provider,driverUno,driverDos,driverTres,driverCuatro,size,nodeId)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/ShutdownNode', methods=['POST','GET'])
def ShutdownNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		nodeId = request.form['nodeId']

		nodes = shutdownNodeFunction.shutdownNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/StartNode', methods=['POST','GET'])
def StartNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		nodeId = request.form['nodeId']

		nodes = startNodeFunction.startNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}

@app.route('/RebootNode', methods=['POST','GET'])
def RebootNode():
 	try:
 		idsNodes = []
 		provider = request.form['provider']
 		driverUno = request.form['driverUno']
 		driverDos = request.form['driverDos']
		driverTres = request.form['driverTres']
		driverCuatro = request.form['driverCuatro']
		nodeId = request.form['nodeId']

		nodes = rebootNodeFunction.rebootNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

 		idsNodes.append(nodes)
 		return idsNodes

 	except Exception as e:
 		return {'error': str(e)}


if __name__ == '__main__':
    app.run(port=5003,debug=True)
