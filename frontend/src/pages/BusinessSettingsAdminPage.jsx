import { useEffect, useState } from "react";
import settingsService from "../services/settingsService";

const BusinessSettingsAdminPage = () => {
  const [settings, setSettings] = useState([]);
  const [form, setForm] = useState({ name: "", value: "" });
  const [editMode, setEditMode] = useState(false);

  useEffect(() => {
    fetchSettings();
  }, []);

  async function fetchSettings() {
    const data = await settingsService.getBusinessSettings();
    setSettings(data);
  }

  function handleChange(e) {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (editMode) {
      await settingsService.updateSetting(form.name, form.value);
    } else {
      await settingsService.createSetting(form.name, form.value);
    }
    setForm({ name: "", value: "" });
    setEditMode(false);
    fetchSettings();
  }

  function handleEdit(setting) {
    setForm(setting);
    setEditMode(true);
  }

  async function handleDelete(setting) {
    await settingsService.deleteSetting(setting.name);
    fetchSettings();
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-semibold mb-6 font-inter">Бизнес-настройки</h1>

      <form onSubmit={handleSubmit} className="mb-8 space-y-4 max-w-md">
        <div>
          <label className="block mb-1 font-medium">Название</label>
          <input
            type="text"
            name="name"
            value={form.name}
            onChange={handleChange}
            disabled={editMode}
            className="w-full border border-gray-300 rounded px-3 py-2"
            required
          />
        </div>
        <div>
          <label className="block mb-1 font-medium">Значение</label>
          <input
            type="text"
            name="value"
            value={form.value}
            onChange={handleChange}
            className="w-full border border-gray-300 rounded px-3 py-2"
            required
          />
        </div>
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {editMode ? "Сохранить" : "Создать"}
        </button>
      </form>

      <div className="overflow-x-auto rounded border border-gray-200 shadow">
        <table className="min-w-full bg-white text-sm">
          <thead className="bg-gray-100 text-left">
            <tr>
              <th className="px-4 py-3">Название</th>
              <th className="px-4 py-3">Значение</th>
              <th className="px-4 py-3">Действия</th>
            </tr>
          </thead>
          <tbody>
            {settings.length === 0 ? (
              <tr>
                <td colSpan="3" className="text-center text-gray-400 py-6">
                  Нет данных
                </td>
              </tr>
            ) : (
              settings.map((setting) => (
                <tr key={setting.name} className="border-t">
                  <td className="px-4 py-3">{setting.name}</td>
                  <td className="px-4 py-3">{setting.value}</td>
                  <td className="px-4 py-3">
                    <div className="flex gap-2">
                      <button
                        onClick={() => handleEdit(setting)}
                        className="text-blue-600 hover:underline"
                      >
                        ✏️
                      </button>
                      <button
                        onClick={() => handleDelete(setting)}
                        className="text-red-600 hover:underline"
                      >
                        🗑
                      </button>
                    </div>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default BusinessSettingsAdminPage;
