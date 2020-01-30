using Microsoft.SqlServer.Server;
using System.Linq;
using System.Xml.Linq;

namespace SQLLibrary.Text
{
    public class TransformXml
    {
        [SqlProcedure]
        public static string RemoveNameSpace(string inputXml)
        {
            XElement xmlDocumentWithoutNs = RemoveAllNamespaces(XElement.Parse(inputXml));
            return xmlDocumentWithoutNs.ToString();
        }
        
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
