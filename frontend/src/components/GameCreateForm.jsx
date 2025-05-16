import { useState } from "react";
import gameService from "../services/gameService";

const GameForm = ({ onCreated }) => {
  const [form, setForm] = useState({
    name: "",
    description: "",
    icon: null,
  });

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: files ? files[0] : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("name", form.name);
    formData.append("description", form.description);
    formData.append("icon", form.icon);

    try {
      await gameService.createGame(formData);
      setForm({ name: "", description: "", icon: null });
      if (onCreated) onCreated(); // обновить список
    } catch (error) {
      console.error("Ошибка при создании игры:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 mb-6">
      <div>
        <label className="block mb-1">Название</label>
        <input
          type="text"
          name="name"
          value={form.name}
          onChange={handleChange}
          className="border p-2 w-full"
          required
        />
      </div>

      <div>
        <label className="block mb-1">Описание</label>
        <textarea
          name="description"
          value={form.description}
          onChange={handleChange}
          className="border p-2 w-full"
          required
        />
      </div>

      <div>
        <label className="block mb-1">Иконка</label>
        <input
          type="file"
          name="icon"
          onChange={handleChange}
          className="border p-2 w-full"
          accept="image/*"
          required
        />
      </div>

      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
        Создать игру
      </button>
    </form>
  );
};

export default GameForm;
