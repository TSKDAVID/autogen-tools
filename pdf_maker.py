def pdf_maker():

    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this path
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    # enable local file access
    options = {
        'enable-local-file-access': '',
        'quiet': ''
    }

    # convert HTML file to PDF
    pdfkit.from_file(f'test.html', f'output.pdf', configuration=config, options=options) #change the 'test.html' and 'output.pdf' into names that you need, test html is a file that needs to e converted and
                                                                                         #and output.pdf is an output file

#in this case this is for windows computer, you would need to install wkhtmltopdf from their website and the file path would still work if you install it in default directory 
#in case you are using mac os you would tipically change that path to: /usr/local/bin/wkhtmltopdf or you could type which wkhtmltopdf and see where it is and put that path
