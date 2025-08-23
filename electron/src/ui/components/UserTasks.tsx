import { IconHistory } from '@tabler/icons-react';
import { useState } from 'react';

export function UserTasks() {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <div className="max-w-lg mx-auto order-1">
      <div className="collapse collapse-arrow bg-base-100 border-base-300 border">
        <input
          type="checkbox"
          checked={isOpen}
          onChange={() => setIsOpen(!isOpen)}
        />

        <div className="collapse-title font-semibold flex items-center gap-2 text-secondary">
          <IconHistory size={24} /> Tasks
        </div>

        <div className="collapse-content text-sm">
          <div className="flex flex-col gap-2 overflow-y-auto max-h-[640px]">
            <p>
              Click the "Sign Up" button in the top right corner and follow the
              registration process.
            </p>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet
              veritatis possimus quis adipisci ducimus, vitae commodi excepturi
              vero at illum voluptates minima quam veniam, nesciunt voluptate!
              Sit sint, reprehenderit doloribus sunt nam non, molestias incidunt
              possimus est, deleniti impedit pariatur minima fugiat quas iure!
              Dolorum, aliquid! Placeat nam dicta eligendi fugiat quam officiis
              repellat fuga possimus. Iste eius aliquid, consequuntur illo saepe
              cupiditate assumenda vitae tenetur ipsum, error fuga possimus quis
              iusto deserunt, illum inventore est autem nam nemo quos delectus?
              Numquam distinctio vel dolore facere quisquam exercitationem unde
              temporibus cumque deserunt. Voluptatem repellendus corporis nemo
              consequuntur et culpa tenetur numquam ullam nam excepturi commodi
              sint saepe distinctio, quidem possimus architecto eveniet illo
              libero pariatur, placeat aut quae aliquid minima totam. Cumque,
              exercitationem, earum ratione voluptatem accusamus excepturi
              facilis hic consequatur enim doloribus obcaecati labore cum fuga,
              molestiae corrupti? Itaque libero accusamus vitae est? Quasi
              dignissimos perferendis voluptate. Tempore qui excepturi adipisci
              sapiente saepe similique porro labore iure dolores molestias
              repudiandae eum nesciunt recusandae, nobis unde perspiciatis
              aliquid mollitia inventore, quibusdam facilis! Sapiente aut
              praesentium alias. Soluta nulla nam deleniti mollitia placeat
              dolor reiciendis exercitationem, cum quaerat cumque labore
              repellat, odio similique sint harum esse doloribus voluptatum
              nostrum voluptas. Est illo reiciendis, error sapiente quia saepe.
              Omnis quo dolor, debitis dolores neque iste aspernatur ipsam
              maiores voluptates blanditiis similique voluptate magnam alias
              inventore totam accusantium? Architecto ut eos, consectetur
              impedit omnis, labore itaque sequi veniam quo reprehenderit
              tempore vel veritatis sint minus quod tempora delectus at eveniet
              ab, illo natus quasi doloremque nostrum. Atque necessitatibus
              quas, ipsa totam magnam, ipsum repellendus officiis distinctio
              voluptate explicabo, velit voluptatibus quo quam molestiae autem
              deserunt. Cumque excepturi tenetur error ipsum est, suscipit
              facilis ipsa nobis illo necessitatibus saepe velit praesentium
              accusamus deleniti sint? Omnis amet odio sit nobis voluptate nam
              dicta cum, rem iste sint voluptatum minus. Voluptates ratione
              eligendi at voluptatum reprehenderit ad et excepturi dolorum!
              Esse, enim excepturi laudantium explicabo incidunt atque quam.
              Repellendus, id? Voluptatem, mollitia nam aspernatur provident
              molestiae dolores. Ab, quis sapiente rem laudantium debitis
              provident vero? Fugiat rerum laudantium officia quasi deserunt
              iusto doloremque ducimus ratione ab possimus aliquam illum
              commodi, alias nemo deleniti hic voluptas fuga sit quis
              consequuntur. Omnis explicabo perferendis sed exercitationem
              cupiditate officiis error incidunt perspiciatis enim commodi quae
              ipsum doloribus beatae temporibus praesentium ad aperiam, suscipit
              molestias corporis in! Et sunt officia adipisci quaerat sint! Nisi
              dolorum ea atque reiciendis velit nobis quasi commodi officiis,
              illum aperiam dignissimos ipsa aliquid, soluta ipsum, facere
              minima. Soluta laboriosam nam modi, labore minima odit natus
              animi. A rerum dolor rem corporis illo recusandae laboriosam
              necessitatibus non aliquid nobis eius, quisquam ea labore magni
              ex! Quis possimus quos iste animi doloribus qui modi, nobis natus
              et quo dolore accusantium enim fugit placeat mollitia
              necessitatibus aperiam ullam cupiditate explicabo, rerum eius iure
              harum. Voluptatem asperiores similique iure labore reprehenderit
              tempore rerum odit assumenda temporibus necessitatibus, quibusdam
              voluptatum dolor minus! Dolores laboriosam quos saepe consequatur
              velit omnis dolorem iste distinctio corporis, fuga molestias
              quisquam nemo? Dignissimos, ad laboriosam!
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
