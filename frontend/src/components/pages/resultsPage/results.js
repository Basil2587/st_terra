import React from "react";
import "../../../index.css";
// import {useRef, useState} from 'react'
import pencil from '../../../img/pencil.svg';

export const ResultsPage = () => {
  return (

        <>

          <PlanMontn />
          <TargetNextMonth />
          <DiaryMonth />
          <TargetMonth />
          <PlanNextMonth />
          <Analytics />
       </>


  );
};

const json = {
  monthPlan: [
    { id: 1, status: 0, data: "Сделать 100 продаж", category: "business" },
    {
      id: 2,
      status: 1,
      data: "Залить разработку по Терре на тестовый сервер",
      category: "business",
    },
    {
      id: 3,
      status: 0,
      data: "Найти мобильного разработчика в проект",
      category: "business",
    },
    {
      id: 4,
      status: 0,
      data: "Вложиться в догикоины",
      category: "investments",
    },
    { id: 5, status: 0, data: "Дочитать книгу", category: "growth" },
    { id: 6, status: 0, data: "Начать бегать по утрам", category: "health" },
  ],
  monthTarget: [
    { id: 1, status: 0, data: "Внедрить медитации", category: "brightness" },
    { id: 2, status: 1, data: "Решить семейное", category: "family" },
    {
      id: 3,
      status: 0,
      data: "Показать ребятам первую MVP SAMO",
      category: "business",
    },
  ],
  nextMonthTarget: [
    { id: 1, data: "Подписать договор с инвесторами", category: "business" },
    { id: 2, data: "всякие цели", category: "brightness" },
    { id: 3, data: "просыпаться раньше", category: "growth" },
  ],
  nextMonthPlan: [
    { id: 1, data: "Встреча с друзьями", category: "friends" },
    { id: 2, data: "Планерка по проекту Samo", category: "business" },
    {
      id: 3,
      data: "Очень важная встреча с инвесторами проекта",
      category: "business",
    },
    { id: 4, data: "Сходить в театр", category: "brightness" },
    { id: 5, data: "Свидание с Машей", category: "family" },
    { id: 6, data: "Записаться на занятия по йоге", category: "health" },
    {
      id: 7,
      data: "Курсы по саморазвитию и самодисциплине",
      category: "growth",
    },
    { id: 8, data: "Волонтерство", category: "charity" },
  ],
  monthDiary: [
    {
      id: 1,
      headline: "Вывод недели",
      data: "Неделя прошла не зря, понравилось высыпаться",
    },
    {
      id: 2,
      headline: "Достижения недели",
      data: "переборол ненависть к найму, прочитал книгу, написал пост в блог",
    },
    { id: 3, headline: "Добрые дела", data: "спас котёнка" },
  ],
};

const EditField = () => {
  // const [check, setCheck] = useState(false)
  // const [progress, setprogress] = useState(100)
  // const [text, setText] = useState(100)

  // const textRef = useRef(null)

  const handleAddText = () => {
    // setText(textRef.current.value)
    console.log(document.querySelector(".add-task-list"));
  };

  return (
    <>
      <div className="add-task-field">
        <select className="add-task-list">
          <option className="category-btn" disabled selected>
            Выберите категорию
          </option>
          <option name="family" className="category-btn family-btn">
            
            Семья
          </option>
          <option name="business" className="category-btn business-btn">
            
            Работа
          </option>
          <option name="health" className="category-btn health-btn">
            
            Здоровье
          </option>
          <option name="investments" className="category-btn investments-btn">
            
            Инвестиции
          </option>
          <option name="growth" className="category-btn growth-btn">
            
            Личный рост
          </option>
          <option name="brightness" className="category-btn brightness-btn">
            
            Яркость жизни
          </option>
          <option name="friends" className="category-btn friends-btn">
            
            Друзья
          </option>
          <option name="charity" className="category-btn charity-btn">
            Благотворительность
          </option>
        </select>
        <div className="">
          <input
            placeholder="Новая цель"
            type="text"
            className="add-task-input"
            rel="textRef"
          />
          <button className="add-task-btn" onClick={handleAddText}>
            
            +
          </button>
        </div>
      </div>

      {/* {
      text 
      ? 
      <label className={item.category + " " + "checkbox"}>
      <input type="checkbox" />
      <span> {text} </span>
    </label>
    } */}
    </>
  );
};

// План месяца

// const PlanMontnItem = () => {
//   return (
//     <label className="sunday checkbox">
//       <input type="checkbox" />
//       <span>Встреча с друзьями</span>
//     </label>
//   );
// };

const planMontnItem = json.monthPlan.map((item, i) => {
  const handleRemoveItem = (event) => {
    json.monthPlan.splice(i, 1);
  };

  return (
    <label key={item.id} className={item.category + " " + "checkbox"}>
      <input type="checkbox" />
      <span> {item.data} </span>
      <i id={i} onClick={handleRemoveItem}> x </i>
    </label>
  );
});

const PlanMontn = () => {
  return (
    <div className="block plan-month_block">
      <div className="headline_block">
        <h2> План месяца </h2>
        <img src={pencil} alt="edit" className="edit" />
      </div>
      <div className="progress-block">
        3 / {json.monthPlan.length}
        <div className="progress-bar">
          <span style={{ width: "50%" }}> </span>
        </div>
      </div>
      <EditField />
      <div className="plan-month_checkbox" id="month_plan">
        {planMontnItem}
      </div>
    </div>
  );
};

// Цель след месяца
// const TargetNextMonthItem = () => {
//   return <li className={json.nextMonthTarget[0].category}>Подписать договор с инвесторами</li>;
// };
const targetNextMonthItem = json.nextMonthTarget.map((item) => {
  return <li className={item.category}> {item.data} </li>;
});

const TargetNextMonth = () => {
  return (
    <div className="block target-next-month_block">
      <div className="headline_block">
        <h2> Цели следующего месяца </h2>
        <img src={pencil} alt="edit" className="edit" />
      </div>
      <div>
        <ul className="block_list" id="next_month_target">
          
          {targetNextMonthItem}
        </ul>
      </div>
    </div>
  );
};

// Дневник месяца

const diaryMonthItem = json.monthDiary.map((item) => {
  return (
    <div className="diary_paragraph">
      <h2> {item.headline} </h2> <p id="conclusion"> {item.data} </p>
    </div>
  );
});
const DiaryMonth = () => {
  return (
    <div className="block diary-month_block">
      <div className="headline_block">
        <h2> Дневник месяца </h2>
        <img src={pencil} alt="edit" className="edit" />
      </div>
      {diaryMonthItem}
    </div>
  );
};

// Цели месяца
// const TargetMonthItem = () => {
//   return (
//     <label className="saturday checkbox">
//       <input type="checkbox" />
//       <span>Волонтерство</span>
//     </label>
//   );
// };
const targetMonthItem = json.monthTarget.map((item) => {
  return (
    <label className={item.category + " " + "checkbox"}>
      <input type="checkbox" />
      <span> {item.data} </span>
    </label>
  );
});

const TargetMonth = () => {
  return (
    <div className="block target-month_block">
      <div className="headline_block">
        <h2> Цели месяца </h2>
        <img src={pencil} alt="edit" className="edit" />
      </div>
      <div className="progress-block">
        1 / 3
        <div className="progress-bar">
          <span style={{ width: "33%" }}> </span>
        </div>
      </div>
      <div className="target-month_checkbox" id="target-month">
        
        {targetMonthItem}
      </div>
    </div>
  );
};

// План следующего месяца

// const PlanNextMonthItem = () => {
//   return <li className="monday">Очень важная встреча с инвесторами проекта</li>;
// };
const planNextMonthItem = json.nextMonthPlan.map((item) => {
  return <li className={item.category}> {item.data} </li>;
});

const PlanNextMonth = () => {
  return (
    <div className="block plan-next-month_block">
      <div className="headline_block">
        <h2> План следующего месяца </h2>
        <img src={pencil} alt="edit" className="edit" />
      </div>
      <div>
        <ul className="block_list" id="next_month_plan">
          
          {planNextMonthItem}
        </ul>
      </div>
    </div>
  );
};

// Аналитика

const Analytics = () => {
  return (
    <div className="block analytics">
      <div className="headline_block">
        <h2> Аналитика </h2>
      </div>
      <div className="analytics_body">
        <div className="analytics_paragraph">
          <p> Вовлечённость </p> <span> 90 % </span>
        </div>
        <div className="analytics_paragraph">
          <p> Привычек выполнено </p> <span> 33 % </span>
        </div>
        <div className="analytics_paragraph">
          <p> Страниц книг прочитано </p> <span> 200 / 1000 </span>
        </div>
        <div className="analytics_paragraph">
          <p> Фильмов просмотрено </p> <span> 1 </span>
        </div>
        <div className="analytics_paragraph">
          <p> Самая прокаченная сфера </p>
          <span className="blue_square"> </span>
        </div>
        <div className="analytics_paragraph">
          <p> Сфера, на которую стоит обратить внимание </p>
          <span className="red_square"> </span>
        </div>
      </div>
    </div>
  );
};

export default ResultsPage;
