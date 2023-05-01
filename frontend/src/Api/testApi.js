/* eslint-disable quotes */
/* eslint-disable indent */
(async () => {
  try {
    const res = await fetch("http://localhost:8000/user-list/");
    console.log(res.ok);
    const data = await res.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  } finally {
    console.log("finalizou");
  }
})();
