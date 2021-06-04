import React, {useState} from 'react';
import './addItem.css';

const AddItem = ({hideModal, toggle, setToggle}) => {

    const [values, setValues] = useState({
        title: '',
        description: '',
        sphere: '',
    });

    // eslint-disable-next-line no-unused-vars
    // const [submitted, setSubmitted] = useState(false);

    const handleTitleInputChange = (event) => {
        event.persist();
        setValues((values) => ({
            ...values,
            title: event.target.value,
        }));
    };

    const handleDescriptionInputChange = (event) => {
        event.persist();
        setValues((values) => ({
            ...values,
            description: event.target.value,
        }));
    };

    const delText = () => {
        setValues({
            title: '',
            description: '',
        })
    }

    const submit = (event) => {
        event.preventDefault();

        // json.books.push(values);
        // setSubmitted(!submitted);

        fetch('http://localhost:8000/api/v1/lists/books', {
            method: 'POST',
            body: JSON.stringify({ values }),
            headers: { 'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        // .then(json => console.log(json))
        setToggle(!toggle)
    }

    let [color, setColor] = useState('#fff');
    const activeOption = (e) => {
        let a = e.target.options[e.target.selectedIndex]
        setValues((values) => ({
            ...values,
            sphere: a.value
        }));

        switch (a.value) {
            case 'none':
                setColor('#fff')
                break
            case 'charity':
                setColor('#FF71D8')
                break
            case 'investments':
                setColor('#81FFB3')
                break
            case 'environmentAndFriends':
                setColor('#FE6D6D')
                break
            case 'brightnessOfLife':
                setColor('#69E4FF')
                break
            case 'healthAndSports':
                setColor('#FFA876')
                break
            case 'businessAndCareer':
                setColor('#64BDFF')
                break
            case 'familyAndLove':
                setColor('#B97EFF')
                break
            case 'personalGrowth':
                setColor('#FBF682')
                break
            default:
                color = '#fff'
        }
    }


    return (
        <form className="form"  onSubmit={submit}>
            <div className="modal-container">
                <div className="modal-content">
                <div onClick={hideModal} className="modal-close"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2 2L12 12" stroke="#25315B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 12.001L12 2.00098" stroke="#25315B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div onClick={delText} className="modal-trash">
                    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5.16667 0V0.833333H1V2.5H1.83333V13.3333C1.83333 13.7754 2.00893 14.1993 2.32149 14.5118C2.63405 14.8244 3.05797 15 3.5 15H11.8333C12.2754 15 12.6993 14.8244 13.0118 14.5118C13.3244 14.1993 13.5 13.7754 13.5 13.3333V2.5H14.3333V0.833333H10.1667V0H5.16667ZM3.5 2.5H11.8333V13.3333H3.5V2.5ZM5.16667 4.16667V11.6667H6.83333V4.16667H5.16667ZM8.5 4.16667V11.6667H10.1667V4.16667H8.5Z" fill="#25315B"/>
                    </svg>
                </div>
                    <div className="modal-data">
                        <input onChange={handleTitleInputChange} id="title" type="text" name="titleBook" value={values.title} className="modal-input" placeholder="Введите название"/>
                        <div className="modal-vector"><svg width="20" height="13" viewBox="0 0 20 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M0 11.5003C0 11.2793 0.0877975 11.0674 0.244078 10.9111C0.400358 10.7548 0.61232 10.667 0.833333 10.667H10.8333C11.0543 10.667 11.2663 10.7548 11.4226 10.9111C11.5789 11.0674 11.6667 11.2793 11.6667 11.5003C11.6667 11.7213 11.5789 11.9333 11.4226 12.0896C11.2663 12.2459 11.0543 12.3337 10.8333 12.3337H0.833333C0.61232 12.3337 0.400358 12.2459 0.244078 12.0896C0.0877975 11.9333 0 11.7213 0 11.5003ZM0 6.50033C0 6.27931 0.0877975 6.06735 0.244078 5.91107C0.400358 5.75479 0.61232 5.66699 0.833333 5.66699H19.1667C19.3877 5.66699 19.5996 5.75479 19.7559 5.91107C19.9122 6.06735 20 6.27931 20 6.50033C20 6.72134 19.9122 6.9333 19.7559 7.08958C19.5996 7.24586 19.3877 7.33366 19.1667 7.33366H0.833333C0.61232 7.33366 0.400358 7.24586 0.244078 7.08958C0.0877975 6.9333 0 6.72134 0 6.50033ZM0 1.50033C0 1.27931 0.0877975 1.06735 0.244078 0.91107C0.400358 0.75479 0.61232 0.666992 0.833333 0.666992H19.1667C19.3877 0.666992 19.5996 0.75479 19.7559 0.91107C19.9122 1.06735 20 1.27931 20 1.50033C20 1.72134 19.9122 1.9333 19.7559 2.08958C19.5996 2.24586 19.3877 2.33366 19.1667 2.33366H0.833333C0.61232 2.33366 0.400358 2.24586 0.244078 2.08958C0.0877975 1.9333 0 1.72134 0 1.50033Z" fill="#25315B"/>
                        </svg>
                        </div>
                        <textarea onChange={handleDescriptionInputChange} id="description" type="text" name="descriptionBook" value={values.description} className=" modal-textarea" placeholder="Добавить описание"></textarea>
                        {/* {submitted && !values.description && !values.title && <span id='description-error'>Пожалуйста, заполните все поля</span>} */}
                    </div>
                    <div className="modal-bottom">
                        <p className="modal-text"><span className="img-pages modal-icon"><svg width="15" height="20" viewBox="0 0 15 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M1.984 0C1.45781 0 0.953171 0.209028 0.5811 0.5811C0.209028 0.953172 0 1.45781 0 1.984V18.024C-2.13214e-06 18.2842 0.0513725 18.5418 0.151176 18.782C0.250979 19.0223 0.397245 19.2405 0.581582 19.4241C0.765919 19.6077 0.984696 19.753 1.22536 19.8519C1.46602 19.9507 1.72383 20.001 1.984 20H14.984V0H1.984ZM13.984 19.2H2.232C1.94907 19.2 1.6776 19.0882 1.47679 18.8888C1.27598 18.6895 1.16211 18.4189 1.16 18.136V17.496C1.16 17.2117 1.27294 16.939 1.47398 16.738C1.67502 16.5369 1.94769 16.424 2.232 16.424H14.016L13.984 19.2Z" fill="#25315B"/>
                        </svg>
                        </span>Всего: 700 страниц</p>
                        <p className="modal-text"><span className="img-read modal-icon"><svg width="15" height="20" viewBox="0 0 15 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M9.64734 5.27296L11.5673 6.23296V0H14.984V20H1.984C1.72383 20.001 1.46602 19.9507 1.22536 19.8519C0.984696 19.753 0.765919 19.6077 0.581582 19.4241C0.397245 19.2405 0.250979 19.0223 0.151176 18.782C0.0513725 18.5418 -2.13202e-06 18.2842 0 18.024V1.984C0 1.45781 0.209028 0.953172 0.5811 0.5811C0.953171 0.209028 1.45781 0 1.984 0H7.72734V6.23296L9.64734 5.27296ZM2.232 19.2H13.984L14.016 16.424H2.232C1.94769 16.424 1.67502 16.5369 1.47398 16.738C1.27294 16.939 1.16 17.2117 1.16 17.496V18.136C1.16211 18.4189 1.27598 18.6895 1.47679 18.8888C1.6776 19.0881 1.94907 19.2 2.232 19.2Z" fill="#25315B"/>
                        </svg>
                        </span>Прочитано: 100 страниц</p>
                        <div className="square" style={{backgroundColor: color}}></div>
                        <select onChange={activeOption} className="form-select modal-text">
                            <option className="none" value='none'>Cфера:</option>
                            <option value='charity'>Cфера:Благотворительность</option>
                            <option value='investments'>Cфера:Инвестиции</option>
                            <option value='environmentAndFriends'>Cфера:Окружение и друзья</option>
                            <option value='brightnessOfLife'>Cфера:Яркость жизни</option>
                            <option value='healthAndSports'>Cфера:Здоровье и спорт</option>
                            <option value='businessAndCareer'>Cфера:Бизнес и карьера</option>
                            <option value='familyAndLove'>Cфера:Семья и любовь</option>
                            <option value='personalGrowth'>Cфера:Личный рост</option>
                        </select>
                        <div className="arrow"></div>
                    </div>
                    <button type="submit" class="btn btn-primary modal-btn">Сохранить</button>
                </div>
            </div>
        </form>
        
    );
}

export default AddItem;