#!"C:\Users\Himanshu Hamal\AppData\Local\Programs\Python\Python35-32\python"

print ("content-type: text/html\n")


print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta name="description" content="" />
<meta name="keywords" content="" />
<title>Fitzroy Catholic Bookshop</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="style.css" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="jquery.dropotron-1.0.js"></script>
<script type="text/javascript" src="jquery.slidertron-1.1.js"></script>
<script type="text/javascript">
	$(function() {
		$('#menu > ul').dropotron({
			mode: 'fade',
			globalOffsetY: 11,
			offsetY: -15
		});
		
	});
</script>
</head>
<body>
<div id="wrapper">
	<div id="header">
		<div id="logo">
			<h1><a href="#">Fitzroy Catholic Bookshop</a></h1>
		</div>
		<div id="slogan">
			<h2>Design by Nirakar</h2>
		</div>
	</div>
	<div id="menu">
		<ul>
			<li class="first">
				<span class="opener">Products<b></b></span>
				<ul>
					<li><a href="#">Books</a></li>
					<li><a href="#">Audio Books</a></li>
					<li><a href="#">Music</a></li>
					<li><a href="#">Video</a></li>
				</ul>
			</li>
			<li><a href="#">Catalogue Maintenance</a></li>
			<li><a href="#">Catalogue Search</a></li>
			<li>
				
			</li>
			
		</ul>
		<br class="clearfix" />
	</div>
	
	<div id="page">
		<div id="content">
			<div class="box">
				<h2>Welcome to maintenance page</h2>
				<p>
					<form action="python\dd_product.py" method="post">
					<fieldset>
						<table>
						<tr>
						<th>Title</th>
						<td><input type="text" name="title"></td>
						</tr>
						<tr>
						<th>ISBN</th>
						<td><input type="text" name="isbn"></td>
						</tr>
						<th>Category</th>
						<td><Select name="category"><option>
							Book
						</option>
						<option>Video</option>
						<option>Music</option>
						<option>Auio_Book</option>
						</Select></td>
						</tr>
						<th>Publisher</th>
						<td><select name="publisher">
							<option>Harper Collins</option>
							<option>Penguins</option>
							<option>Orbis</option>
							<option>St. Pauls Publication</option>
						</select></td>
						</tr>
						<th>Author/Artist</th>
						<td><input type="text" name="author"></td>
						</tr>
						<th>Price</th>
						<td><input type="text" name="price"></td>
						</tr>
						<th>Quantity</th>
						<td><input type="number" name="quantity"></td>
						</tr>
						<tr>
						<td colspan="2"><input type="submit" value="Insert"></td>
						</tr>
						</table>
					</fieldset>
					</form>
				</p>
			</div>
			<div class="box" id="content-box1">
				<h3>Mauris justo</h3>
				<ul class="section-list">
					<li class="first">
						<img class="pic alignleft" src="images/pic01.jpg" width="70" height="70" alt="" />
						<span>Condimentum et porttitor tristique nec aliquet magnis pretium quam nibh.</span>
					</li>
					<li>
						<img class="pic alignleft" src="images/pic02.jpg" width="70" height="70" alt="" />
						<span>Posuere elementum sapien justo tortor nulla fringilla suspendisse nascetur.</span>
					</li>
					<li class="last">
						<img class="pic alignleft" src="images/pic03.jpg" width="70" height="70" alt="" />
						<span>Ipsum quis vestibulum feugiat congue nunc laoreet volutpat lorem ipsum sociis.</span>
					</li>
				</ul>
			</div>
			<div class="box" id="content-box2">
				<h3>Magnis hendrerit erat</h3>
				<p>
					Neque neque ornare penatibus tristique fusce turpis. Purus sagittis euismod at ornare suscipit tempus.
				</p>
				<ul class="list">
					<li class="first"><a href="#">Ipsum phasellus ullamcorper</a></li>
					<li><a href="#">Mollis mattis tempus amet</a></li>
					<li><a href="#">Ipsum aliquet dignissim vitae</a></li>
					<li><a href="#">Orci metus curae sed mollis</a></li>
					<li class="last"><a href="#">Tristique amet venenatis</a></li>
				</ul>
			</div>
			<br class="clearfix" />
		</div>
		<div id="sidebar">
			<div class="box">
				<h3>Cursus magnis</h3>
				<ul class="list">
					<li class="first"><a href="#">Adipiscing tincidunt</a></li>
					<li><a href="#">Euismod elit sollicitudin</a></li>
					<li><a href="#">Dolor magnis et lacinia</a></li>
					<li><a href="#">Mauris ornare aenean</a></li>
					<li class="last"><a href="#">Ante semper fringilla</a></li>
				</ul>
			</div>
			<div class="box">
				<h3>Morbi at varius</h3>
				<div class="date-list">
					<ul class="list date-list">
						<li class="first"><span class="date">2/08</span> <a href="#">Quam sed tempus</a></li>
						<li><span class="date">2/05</span> <a href="#">Lorem et vestibulum</a></li>
						<li><span class="date">2/01</span> <a href="#">Risus aenean tellus</a></li>
						<li class="last"><span class="date">1/31</span> <a href="#">Tristique et primis</a></li>
					</ul>
				</div>
			</div>
		</div>
		<br class="clearfix" />
	</div>
	<div id="page-bottom">
		<div id="page-bottom-content">
			<h3>Magnis hendrerit erat</h3>
			<p>
				Euismod sodales sociis hendrerit pulvinar acursus urna. Consectetur egestas sodales at ornare laoreet turpis. Lorem id sapien ridiculus sagittis imperdiet urna suspendisse. Posuere arcu parturient quam risus. Aliquam nullam magnis integer gravida vulputate felis. Consectetur montes sollicitudin dictum. Auctor sociis hendrerit pulvinar acursus urna lorem ipsum dolor vivamus pulvinar libero. Massa egestas cubilia lacus augue mattis consectetur.
			</p>
		</div>
		<div id="page-bottom-sidebar">
			<h3>Sed interdum</h3>
			<ul class="list">
				<li class="first"><a href="#">Suspendisse ultricies</a></li>
				<li><a href="#">Tortor mollis enim</a></li>
				<li class="last"><a href="#">Lorem enim tempor</a></li>
			</ul>
		</div>
		<br class="clearfix" />
	</div>
</div>
<div id="footer">
	&copy; Untitled. All rights reserved. Design by <a href="http://templated.co" rel="nofollow">TEMPLATED</a>. Photos by <a href="http://fotogrph.com/">Fotogrph</a>.
</div>
</body>
</html>
""")