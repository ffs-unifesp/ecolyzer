from ecolyzer.parser import JavaParser
import os

def test_extract_operations():
	javafile = os.path.join(os.path.dirname(__file__), '../data', 'FileSerializer.java')
	src = open(javafile).read()
	parser = JavaParser()
	parser.parser(src)
	operations = parser.extract_operations()[0]['operations']

	src_operations = {
		'extends.FileSerializer': True,	
		'FileSerializer': True,
		'FileSerializer.getPostProcessor': True,
		'FileSerializer.setPostProcessor': True,
		'FileSerializer.generateFile': True,
		'FileSerializer.getPropertiesList': True,
		'FileSerializer.formatValue': True,
		'FileSerializer.isAllowedGetter': True,
	}

	assert len(operations) == len(src_operations)

	for op in operations:
		assert src_operations[op['name']]

def test_internal_class_operations():
	javafile = os.path.join(os.path.dirname(__file__), '../data', 'JFreeChartJFreeChartInfo.java')
	src = open(javafile).read()
	parser = JavaParser()
	parser.parser(src)
	classes = parser.extract_operations()

	assert len(classes) == 2

	operations = classes[0]['operations']
	src_operations = {
		'extends.JFreeChart': True,
		'JFreeChart': True,
		'JFreeChart.isCompatibleValue': True,
		'JFreeChart.getRenderingHints': True,
		'JFreeChart.setRenderingHints': True,
		'JFreeChart.isBorderVisible': True,
		'JFreeChart.setBorderVisible': True,
		'JFreeChart.getBorderStroke': True,
		'JFreeChart.setBorderStroke': True,
		'JFreeChart.getBorderPaint': True,
		'JFreeChart.setBorderPaint': True,
		'JFreeChart.getPadding': True,
		'JFreeChart.setPadding': True,
		'JFreeChart.getTitle': True,
		'JFreeChart.setTitle': True,
		'JFreeChart.addLegend': True,
		'JFreeChart.getLegend': True,
		'JFreeChart.removeLegend': True,
		'JFreeChart.setSubtitles': True,
		'JFreeChart.getSubtitles': True,
		'JFreeChart.getSubtitleCount': True,
		'JFreeChart.getSubtitle': True,
		'JFreeChart.addSubtitle': True,
		'JFreeChart.clearSubtitles': True,
		'JFreeChart.removeSubtitle': True,
		'JFreeChart.getPlot': True,
		'JFreeChart.getCategoryPlot': True,
		'JFreeChart.getXYPlot': True,
		'JFreeChart.getAntiAlias': True,
		'JFreeChart.setAntiAlias': True,
		'JFreeChart.getTextAntiAlias': True,
		'JFreeChart.setTextAntiAlias': True,
		'JFreeChart.getBackgroundPaint': True,
		'JFreeChart.setBackgroundPaint': True,
		'JFreeChart.getBackgroundImage': True,
		'JFreeChart.setBackgroundImage': True,
		'JFreeChart.getBackgroundImageAlignment': True,
		'JFreeChart.setBackgroundImageAlignment': True,
		'JFreeChart.getBackgroundImageAlpha': True,
		'JFreeChart.setBackgroundImageAlpha': True,
		'JFreeChart.isNotify': True,
		'JFreeChart.setNotify': True,
		'JFreeChart.draw': True,
		'JFreeChart.createAlignedRectangle2D': True,
		'JFreeChart.drawTitle': True,
		'JFreeChart.createBufferedImage': True,
		'JFreeChart.handleClick': True,
		'JFreeChart.addChangeListener': True,
		'JFreeChart.removeChangeListener': True,
		'JFreeChart.fireChartChanged': True,
		'JFreeChart.notifyListeners': True,
		'JFreeChart.addProgressListener': True,
		'JFreeChart.removeProgressListener': True,
		'JFreeChart.notifyListeners': True,
		'JFreeChart.titleChanged': True,
		'JFreeChart.plotChanged': True,
		'JFreeChart.equals': True,
		'JFreeChart.writeObject': True,
		'JFreeChart.readObject': True,
		'JFreeChart.main': True,
		'JFreeChart.clone': True,
	}

	assert len(operations) == 72 == len(src_operations) + 12 

	for op in operations:
		assert src_operations[op['name']]		
		#print(f'\'{op["name"]}\': True,')

	operations = classes[1]['operations']	
	src_operations = {
		'extends.JFreeChartInfo': True,
		'JFreeChartInfo': True,
		'JFreeChartInfo.getLogo': True
	}
	
	assert len(operations) == 3 == len(src_operations)

	for op in operations:
		assert src_operations[op['name']]		
		# print(f'\'{op["name"]}\': True,')	

def test_extract_calls():
	javafile = os.path.join(os.path.dirname(__file__), '../data', 'FileSerializer.java')
	src = open(javafile).read()
	parser = JavaParser()
	parser.parser(src)
	calls = parser.extract_calls()

	src_calls = {
		'DataFormatter.formatData': {'caller': 'df'},
		'FileSerializer.getPropertiesList': {'caller': ''},
		'PostProcessor.postProcess': {'caller': 'pp'},
		'FileOutputStream': {'caller': 'new'},
		'FileOutputStream.write': {'caller': 'fileout'},
		'FileOutputStream.close': {'caller': 'fileout'},
		'RuntimeException': {'caller': 'new'},
		'HashMap': {'caller': 'new'},
		'Object.getClass': {'caller': 'obj'},
		'Class.getMethods': {'caller': 'clas'},
		'FileSerializer.isAllowedGetter': {'caller': ''},
		'Method.invoke': {'caller': 'm'},
		'Method.getName': {'caller': 'm'},
		'String.substring': {'caller': 'getterName'},
		'String.substring': {'caller': 'getterName'},
		'FileSerializer.formatValue': {'caller': ''},
		'Map.put': {'caller': 'props'},
		'RuntimeException': {'caller': 'new'},
		'InstantiationException': {'caller': 'throws'},
		'IllegalAccessException': {'caller': 'throws'},
		'Method.getAnnotations': {'caller': 'm'},
		'Annotation.annotationType': {'caller': 'an'},
		'Class.isAnnotationPresent': {'caller': 'anType'},
		'Class.getAnnotation': {'caller': 'anType'},
		'FormatterImplementation.value': {'caller': 'fi'},
		'Class.newInstance': {'caller': 'c'},
		'ValueFormatter.readAnnotation': {'caller': 'vf'},
		'ValueFormatter.formatValue': {'caller': 'vf'},
		'Method.getName': {'caller': 'm'},
		'Method.getParameterTypes': {'caller': 'm'},
		'Method.getReturnType': {'caller': 'm'},
		'Method.getName': {'caller': 'm'},
		'Method.isAnnotationPresent': {'caller': 'm'},
		'Override': {'caller': '@'},
		'Override': {'caller': '@'},
		'implements.Serializer': {'caller': 'implements'},
		#'toLowerCase': True, # method chaining doesn't work
		#'startsWith': True, # method chaining doesn't work
		# 'equals': True, # method chaining doesn't work
		# 'Override': True, #TODO: Annotation call
	}

	for call in calls:
		assert src_calls[call['ref']]
		assert src_calls[call['ref']]['caller'] != None
		#print(f'\'{call["call"]}\': {{\'caller\': \'{call["caller"]}\'}},')

	assert len(calls) == 36 == len(src_calls) + 5 # 5 repeated calls	

def test_extract_associations():
	javafile = os.path.join(os.path.dirname(__file__), '../data', 'FileSerializer.java')
	src = open(javafile).read()
	parser = JavaParser()
	parser.parser(src)
	assocs = parser.extract_associations()

	src_assocs = {
		'java/io/FileOutputStream': True,
		'java/lang/annotation/Annotation': True,
		'java/lang/reflect/InvocationTargetException': True,
		'java/lang/reflect/Method': True,
		'java/util/HashMap': True,
		'java/util/Map': True
	}

	assert len(src_assocs) == len(assocs)

	for assoc in assocs:
		assert src_assocs[assoc]		
		#print('\'' + assoc + '\': ' + 'True,')