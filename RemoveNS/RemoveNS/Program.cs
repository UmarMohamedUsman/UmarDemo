using System;
using System.ComponentModel.DataAnnotations;
using System.Xml;
using System.Xml.Linq;
using System.Linq;
using System.IO;

namespace RemoveNS
{
    class Program
    {
        static void Main(string[] args)
        {
            var soapFile = @"C:\Temp\soap-req1.xml";
            var doc = XDocument.Load(soapFile);
            var output = RemoveAllNamespaces(doc.ToString());

            StreamWriter sw = new StreamWriter(@"c:\temp\1.xml");
            sw.Write(output);
            sw.Close();

            //Console.WriteLine(output);
            Console.Read();
        }


        public static string RemoveAllNamespaces(string xmlDocument)
        {
            XElement xmlDocumentWithoutNs = RemoveAllNamespaces(XElement.Parse(xmlDocument));

            return xmlDocumentWithoutNs.ToString();
        }

        //Core recursion function
        private static XElement RemoveAllNamespaces(XElement xmlDocument)
        {
            if (!xmlDocument.HasElements)
            {
                XElement xElement = new XElement(xmlDocument.Name.LocalName);
                xElement.Value = xmlDocument.Value;

                foreach (XAttribute attribute in xmlDocument.Attributes())
                    xElement.Add(attribute);

                return xElement;
            }
            return new XElement(xmlDocument.Name.LocalName, xmlDocument.Elements().Select(el => RemoveAllNamespaces(el)));
        }

    }
}
