using System;
using System.Data.SqlClient;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.Azure.WebJobs.Host;
using Newtonsoft.Json;

namespace Contoso.Expenses.Functions
{
    public static class ExpenseAutoApproveFunction
    {
        [FunctionName("ExpenseAutoApproveFunction")]
        public static void Run([QueueTrigger("contosoexpenses", Connection = "StorageConnectionString")]string expenseItem, TraceWriter log)
        {
            var expense = JsonConvert.DeserializeObject<ExpenseExtended>(expenseItem);

            if (expense != null && expense.Status == ApprovalStatus.New)
            {
                expense.Status = expense.Amount <= 50.0 ? ApprovalStatus.Paid : ApprovalStatus.Pending;
            }

            var sqlConnection = System.Configuration.ConfigurationManager.ConnectionStrings["SQLConnection"].ConnectionString;

            using (var connection = new SqlConnection(sqlConnection))
            {
                using (var command = connection.CreateCommand())
                {
                    command.CommandText = "UPDATE Expense SET Status = @status WHERE ExpenseId = @id";
                    command.Parameters.AddWithValue("@id", expense.ExpenseId);
                    command.Parameters.AddWithValue("@status", (int)expense.Status);

                    connection.Open();
                    command.ExecuteNonQuery();
                    connection.Close();
                }
            }

            log.Info($"Expense status set to: {expense.Status.ToString()}");
        }
    }

    public enum ApprovalStatus : int
    {
        New = 0,
        Pending = 1,
        Paid = 2
    }

    public class ExpenseExtended
    {
        public int ExpenseId { get; set; }
        public string Purpose { get; set; }
        public Nullable<System.DateTime> Date { get; set; }
        public string Cost_Center { get; set; }
        public Nullable<double> Amount { get; set; }
        public string Approver { get; set; }
        public string Receipt { get; set; }
        public string ApproverEmail { get; set; }
        public ApprovalStatus Status { get; set; }
    }
}
