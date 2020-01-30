using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;
using SQLLibrary.Text;

namespace TestConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var soapFile = @"C:\Temp\soap-req1.xml";
            var doc = XDocument.Load(soapFile);

            var output = TransformXml.RemoveNameSpace(doc.ToString());

            StreamWriter sw = new StreamWriter(@"c:\temp\1.xml");
            sw.Write(output);
            sw.Close();

            Console.Read();
        }
    }
}
