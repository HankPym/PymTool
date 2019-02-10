$filename = $ARGV[0];
$outfilename = $filename . "\.xml";

open (INFILE, "<$filename") or die;

open (OUTFILE, ">$outfilename") or die;

print OUTFILE "\<\?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"\?\>\n<CampaignOrders xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\n";

foreach (<INFILE>)
{
	$line = $_;
    chomp ($line);
	$line =~ /(\.+)\t(\.+)\t(\.+)/;
	print  "$1 $2 $3";
}

close INFILE;
close OUTFILE;