import { IconPhotoFilled } from '@tabler/icons-react';
import { useState } from 'react';
import { AdvanceSettings, UserTasks } from '../components';
import styles from './AppMain.module.css';
import { Carousel } from '../components/templates';
// import temp1_img from '../assets/temp/temp1.png';
// import temp2_img from '../assets/temp/temp2.png';
// import temp3_img from '../assets/temp/temp3.png';
// import temp4_img from '../assets/temp/temp4.png';
// import temp5_img from '../assets/temp/temp5.png';
// import temp6_img from '../assets/temp/temp6.png';

export function AppMain() {
  const [images] = useState([
    // temp1_img,
    // temp2_img,
    // temp3_img,
    // temp4_img,
    // temp5_img,
    // temp6_img,
  ]);

  return (
    <main className={`${styles.main} ${styles['dotted-background']}`}>
      <div className={styles['main-container']}>
        <div className="order-1">
          <UserTasks />
        </div>

        <div className="order-2 xl:order-3">
          <AdvanceSettings />
        </div>

        <div className="flex flex-col gap-4 w-full max-w-lg mx-auto xl:max-w-none order-3 xl:order-2">
          <div className="flex flex-col gap-4">
            <div
              className={
                styles['moving-border'] +
                ' relative bg-base-100 rounded-md border border-base-300 p-1 overflow-hidden'
              }
            >
              <textarea
                className="textarea resize-none h-32 w-full border-secondary focus-visible:outline-secondary relative z-10"
                placeholder="You can generate images by entering prompts here."
              ></textarea>
            </div>

            <div className="flex justify-between">
              <div></div>

              <button className="flex gap-4 btn btn-secondary">
                <IconPhotoFilled />
                <span>Generate Image</span>
              </button>
            </div>
          </div>

          <div className="flex-1 flex justify-center items-center">
            <Carousel images={images} />
          </div>
        </div>
      </div>
    </main>
  );
}
