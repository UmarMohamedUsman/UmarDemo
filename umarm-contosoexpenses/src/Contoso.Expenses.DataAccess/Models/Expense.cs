//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace Contoso.Expenses.DataAccess.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class Expense
    {
        public int ExpenseId { get; set; }
        public string Purpose { get; set; }
        public Nullable<System.DateTime> Date { get; set; }
        public string Cost_Center { get; set; }
        public Nullable<double> Amount { get; set; }
        public string Approver { get; set; }
        public string Receipt { get; set; }
        public ApprovalStatus Status { get; set; }
    }
}
