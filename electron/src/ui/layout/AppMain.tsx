import {
  IconChevronLeft,
  IconChevronRight,
  IconDots,
  IconPhotoFilled,
  IconSearch,
} from '@tabler/icons-react';
import { useState } from 'react';
import { AdvanceSettings, UserTasks } from '../components';
import styles from './AppMain.module.css';
import temp1_img from '../assets/temp/temp1.jpeg';
import temp2_img from '../assets/temp/temp2.jpeg';
import temp3_img from '../assets/temp/temp3.jpeg';
import temp4_img from '../assets/temp/temp4.jpeg';
import temp5_img from '../assets/temp/temp5.jpeg';
import temp6_img from '../assets/temp/temp6.jpeg';

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
      <div className="order-1">
        <UserTasks />
      </div>

      <div className="flex flex-col gap-4 w-full max-w-lg mx-auto xl:max-w-none order-3 xl:order-2">
        <div className="flex flex-col gap-4">
          <textarea
            className="textarea resize-none h-32 w-full"
            placeholder="You can generate images by entering prompts here."
          ></textarea>

          <div className="flex justify-between">
            <div></div>

            <button className="flex gap-4 btn btn-secondary">
              <IconPhotoFilled />
              <span>Generate Image</span>
            </button>
          </div>
        </div>

        <div className="flex-1 flex justify-center items-center">
          <div className="carousel w-full max-w-md h-full max-h-[448px] mx-auto rounded-lg border border-base-300 bg-base-300/50">
            {images.length > 0 ? (
              <>
                {images.map((url, i) => (
                  <div
                    key={i}
                    id={`slide${i}`}
                    className="carousel-item relative w-full"
                  >
                    <img src={url} className="w-full object-cover object-top" />

                    <div className="absolute left-0 right-0 top-0 p-4 flex justify-end">
                      <button className="btn btn-primary btn-circle btn-soft">
                        <IconDots />
                      </button>
                    </div>

                    <div className="absolute left-0 right-0 bottom-0 p-4 flex justify-between">
                      <a
                        href={`#slide${
                          i - 1 === -1 ? images.length - 1 : i - 1
                        }`}
                        className="btn btn-primary btn-circle btn-soft"
                      >
                        <IconChevronLeft />
                      </a>

                      <button className="btn btn-primary btn-circle btn-soft">
                        <IconSearch />
                      </button>

                      <a
                        href={`#slide${
                          i + 2 === images.length + 1 ? 0 : i + 1
                        }`}
                        className="btn btn-primary btn-circle btn-soft"
                      >
                        <IconChevronRight />
                      </a>
                    </div>
                  </div>
                ))}
              </>
            ) : (
              <div className="w-full h-full flex justify-center items-center">
                <IconPhotoFilled className="size-8 text-secondary/25" />
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="order-2 xl:order-3">
        <AdvanceSettings />
      </div>
    </main>
  );
}
