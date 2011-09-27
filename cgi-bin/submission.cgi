#!/usr/bin/perl  -wT

use strict;

use CGI qw(:standard escapeHTML);

# File to append submissions to
open (my $FH, ">>networks.txt");
flock ($FH, 2);

# store date
param("_timestamp", scalar localtime);

# Use CGI to write submission to file
save_parameters($FH);

my $name = param('name');



my $heredoc = <<END;
		<div id="wrap">
			<div id="header">
				<table class="header">
					<tr>
						<td>
							<img src="../UoA_col_horz.png" />
						</td>
						<td>
							<h1>
								The Internet Topology Zoo
							</h1>
						</td>
					</tr>
				</table>
			</div>
			<div id="main">
				<div id="sidebar">
					<ul>
						<li>
							<a href="../index.html">Home</a>
						</li>
						<li>
							<a href="../dataset.html">Dataset</a>
						</li>       
						<li>
							<a href="../gallery.html">Gallery</a>
						</li>
						<li>
							<a href="../publications.html">Publications</a>
						</li>
						<li>
							<a href="../toolset.html">Toolset</a>
						</li>
						<li>
							<a href="../documentation.html">Documentation</a>
						</li>
						<li>
							<a href="../contribute.html">Contribute</a>
						</li>
						<li>
							<a href="../links.html">External Links</a>
						</li>
						<li>
							<a href="../contact.html">Contact</a>
						</li>
					</ul>
				</div>
				<div id="main-content">  
					<h2> Contribute</h2>    
END


print header();
print start_html( -title=>"The Internet Topology Zoo",
  -style=>{-src=>'../blue/style.css'},);

print $heredoc; 


print "Thank you " . $name . " for your submission.<br>\n";
print end_html();
