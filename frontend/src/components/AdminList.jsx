const AdminList = ({ columns, data }) => {
    return (
      <div className="overflow-x-auto rounded-2xl border border-gray-200 shadow">
        <table className="min-w-full bg-white text-sm font-inter">
          <thead className="bg-oneWinBlue-600 text-white">
            <tr>
              {columns.map((col) => (
                <th key={col.key} className="text-left px-4 py-3 whitespace-nowrap">
                  {col.title}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.length === 0 ? (
              <tr>
                <td colSpan={columns.length} className="text-center text-gray-400 py-6">
                  Нет данных для отображения
                </td>
              </tr>
            ) : (
              data.map((row, rowIndex) => (
                <tr
                  key={rowIndex}
                  className={rowIndex % 2 === 0 ? "bg-gray-50" : "bg-white"}
                >
                  {columns.map((col) => (
                    <td key={col.key} className="px-4 py-3 whitespace-nowrap">
                      {col.render ? col.render(row[col.key], row) : row[col.key]}
                    </td>
                  ))}
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    );
  };
  
  export default AdminList;
  