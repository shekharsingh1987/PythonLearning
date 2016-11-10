using Microsoft.SqlServer.Management.Smo;

namespace Orion.CodeLibrary.DBReportsRestore
{
    public interface IDBRestore
    {
        event RestoreDelegates.OnDBRestoreHandler OnDBRestore;
        int ConnectionStatementTimeout { get; set; }
        void RestoreDB(string connectionString, string backupFile);
    }
}
