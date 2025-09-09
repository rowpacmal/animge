import {
  IconChevronLeft,
  IconChevronRight,
  IconDots,
  IconPhotoFilled,
  IconSearch,
} from '@tabler/icons-react';

export function Carousel({ images }: { images: string[] }) {
  return (
    <div className="carousel w-full max-w-md h-full max-h-[448px] mx-auto rounded-lg border border-primary bg-base-300/50">
      {images.length > 0 ? (
        <>
          {images.map((image, i) => (
            <div
              key={i}
              id={`slide${i}`}
              className="carousel-item relative w-full"
            >
              <img src={image} className="w-full object-cover object-top" />

              <div className="absolute left-0 right-0 top-0 p-4 flex justify-between">
                <p className="text-sm text-primary bg-base-100 rounded-lg py-1 px-2 h-fit">
                  {i + 1} / {images.length}
                </p>

                <button className="btn btn-primary btn-circle btn-soft">
                  <IconDots />
                </button>
              </div>

              <div className="absolute left-0 right-0 bottom-0 p-4 flex justify-between">
                {images.length > 1 && (
                  <a
                    href={`#slide${i - 1 === -1 ? images.length - 1 : i - 1}`}
                    className="btn btn-primary btn-circle btn-soft"
                  >
                    <IconChevronLeft />
                  </a>
                )}

                <button className="btn btn-primary btn-circle btn-soft mx-auto">
                  <IconSearch />
                </button>

                {images.length > 1 && (
                  <a
                    href={`#slide${i + 2 === images.length + 1 ? 0 : i + 1}`}
                    className="btn btn-primary btn-circle btn-soft"
                  >
                    <IconChevronRight />
                  </a>
                )}
              </div>
            </div>
          ))}
        </>
      ) : (
        <div className="w-full h-full min-h-[448px] flex justify-center items-center">
          <IconPhotoFilled className="size-8 text-primary" />
        </div>
      )}
    </div>
  );
}
