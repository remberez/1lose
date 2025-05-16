import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import gameService from "../services/gameService";

const GameEditPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    description: "",
    icon: null,
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchGame() {
      try {
        const data = await gameService.getGameById(id);
        setForm({
          name: data.name || "",
          description: data.description || "",
          icon: null,
        });
        setLoading(false);
      } catch (error) {
        console.error("Ошибка при загрузке игры", error);
      }
    }

    fetchGame();
  }, [id]);

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
    if (form.icon) formData.append("icon", form.icon);

    try {
      await gameService.updateGame(id, formData);
      navigate("/admin/games");
    } catch (error) {
      console.error("Ошибка при обновлении игры", error);
    }
  };

  if (loading) return <div>Загрузка...</div>;

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Редактирование игры</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
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
          <label className="block mb-1">Новая иконка (если нужно)</label>
          <input
            type="file"
            name="icon"
            onChange={handleChange}
            className="border p-2 w-full"
            accept="image/*"
          />
        </div>

        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
          Сохранить изменения
        </button>
      </form>
    </div>
  );
};

export default GameEditPage;
