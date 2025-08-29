import { IconHistory } from '@tabler/icons-react';
import { Collapse } from './templates';
import { useEffect, useState } from 'react';

export function UserTasks() {
  const [tasks, setTasks] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    (async function () {
      try {
        setIsLoading(true);
        const temp = await (window as any).electron.getTempFolder();
        // console.log('tasks: ', temp);
        setTasks(temp.sort((a: any, b: any) => b.timestamp - a.timestamp));
      } catch (error) {
        console.error(error);
      } finally {
        setIsLoading(false);
      }
    })();
  }, []);

  return (
    <Collapse icon={<IconHistory />} title="User Tasks">
      {isLoading ? (
        <div className="flex justify-center items-center gap-2 text-primary py-4">
          <div className="loading loading-ring"></div>

          <p>Loading tasks...</p>
        </div>
      ) : (
        <>
          {tasks.map(
            ({
              name,
              children,
            }: {
              name: string;
              children: { path: string }[];
            }) => (
              <div key={name} className="flex flex-col bg-base-200 rounded-box">
                <div className="grid grid-cols-[auto_1fr_auto] items-center gap-2 py-2 px-3 bg-base-300 text-primary rounded-t-box">
                  <IconHistory />

                  <h3 className="font-semibold truncate">{name}</h3>

                  <button className="btn btn-primary btn-xs">Details</button>
                </div>

                <div className="relative">
                  <div className="stack stack-end p-2 border border-base-300 rounded-b-box">
                    {children.map(({ path }, i: number) => {
                      return (
                        <img
                          key={i}
                          src={path}
                          className="w-full aspect-[2/1] object-cover rounded-box border border-primary"
                        />
                      );
                    })}
                  </div>

                  <p className="absolute top-0 left-0 flex gap-2  text-sm text-primary bg-base-200 border border-base-300 rounded-lg py-1 px-2 h-fit z-10 m-4 shadow">
                    {children.length}
                  </p>
                </div>
              </div>
            )
          )}
        </>
      )}
    </Collapse>
  );
}
